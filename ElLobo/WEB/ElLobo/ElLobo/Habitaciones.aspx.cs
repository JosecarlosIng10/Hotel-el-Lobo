using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Xml;

namespace ElLobo
{
    public partial class Habitaciones : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {

          
        }
       
        protected void Button2_Click(object sender, EventArgs e)
        {
            TextBox1.Text = "";
            if (FileUploadControl.HasFile)
            {
                try
                {
                    string filename = Path.GetFileName(FileUploadControl.FileName);
                    FileUploadControl.SaveAs(Server.MapPath("~/") + filename);
                   
                    StreamReader sr = new StreamReader(Server.MapPath("~/") + filename);
                    string contenido = sr.ReadToEnd();
                    sr.Close();
                    TextBox1.Text = contenido;
                    string nivel = "";
                    string numero = "";
                    XmlDocument myXmlDocument = new XmlDocument();
                    myXmlDocument.Load(Server.MapPath("~/") + filename);


                    XmlNode node = myXmlDocument.DocumentElement;

                    foreach (XmlNode node1 in node.ChildNodes)

                        if (node1.Name == "habitacion")
                        {
                            nivel = node1.FirstChild.InnerText;
                            numero = node1.LastChild.InnerText;
                            guardar(nivel, numero);
                        }


                    HttpContext.Current.Response.Write("<script>window.alert('Habitaciones Guardadas');</script>");


                }
                catch (Exception ex)
                {
                    HttpContext.Current.Response.Write("<script>window.alert('Error al subir archivo');</script>");
                }
            }
        }

        protected void Button3_Click(object sender, EventArgs e)
        {
           

        }

        public void guardar(string nivel, string numero)
        {
            try
            {
                using (var client = new WebClient())
                {
                    var values = new NameValueCollection();
                    values["nivel"] = nivel;
                    values["numero"] = numero;

                    var response = client.UploadValues("http://192.168.1.7:5000/Habitacion", values);
                    var responseString = Encoding.Default.GetString(response);

                    if (responseString != "True")
                    {
                        HttpContext.Current.Response.Write("<script>window.alert('Error al guardar las habitaciones');</script>");

                    }
                   



                }

            }
            catch
            {
                HttpContext.Current.Response.Write("<script>window.alert('Problema con la peticion');</script>");
            }
        }
    }
}