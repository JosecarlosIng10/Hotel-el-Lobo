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
    public partial class Reservaciones : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
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
                    string usuario = "";
                    string tarjeta = "";
                    string habitacion = "";
                   
                    
                    string fechai = "";
                    string fechaf = "";


                    XmlDocument myXmlDocument = new XmlDocument();
                    myXmlDocument.Load(Server.MapPath("~/") + filename);


                    XmlNode node = myXmlDocument.DocumentElement;

                    foreach (XmlNode node1 in node.ChildNodes)

                        if (node1.Name == "reservacion")
                        {
                            int cont = 0;
                            int costos = 0;
                            usuario = node1.FirstChild.InnerText;
                            tarjeta = node1.FirstChild.NextSibling.InnerText;
                            habitacion= node1.FirstChild.NextSibling.NextSibling.InnerText;

                            
                                XmlNode extras = node1.FirstChild.NextSibling.NextSibling.NextSibling;



                                foreach (XmlNode node2 in extras.ChildNodes)
                                    if (node2.Name == "extra")
                                    {
                                        cont++;
                                    }



                            if (extras.Name.Equals("fechaIngreso"))
                            {
                                fechai = extras.InnerText;
                            }
                            else
                            {

                                fechai = node1.FirstChild.NextSibling.NextSibling.NextSibling.NextSibling.InnerText;

                            }
                            
                            try
                            {
                                fechaf = node1.FirstChild.NextSibling.NextSibling.NextSibling.NextSibling.NextSibling.InnerText;
                            }
                            catch
                            {
                                fechaf = "";
                            }
                            char[] hab = habitacion.ToCharArray();
                            int numeropiso = Convert.ToInt32(hab[0]+"");
                            int nume = Convert.ToInt32(hab[1] +""+ hab[2]);
                            
                            costos = (numeropiso * 200) + nume;
                            for (int i = 0; i < cont; i++) {
                                if (i > 2) {
                                    costos += 50;
                                }
                                else
                                {
                                    costos += 75;
                                }
                            }
                            char[] fecha = fechai.ToCharArray();

                            string year = fecha[0] +"" +fecha[1] + fecha[2] + fecha[3];
                            string mes = fecha[4] +""+ fecha[5];
                            string dia = fecha[6] +""+ fecha[7];

                            guardarCosto(tarjeta, costos);
                            guardarBitacora(usuario, tarjeta, costos, habitacion, fechai, fechaf);
                            guardarDispersa(mes, year, dia, usuario, tarjeta, habitacion);
                        }

                    HttpContext.Current.Response.Write("<script>window.alert('Habitaciones Guardadas');</script>");


                }
                catch (Exception ex)
                {
                    HttpContext.Current.Response.Write("<script>window.alert('Error al subir archivo');</script>");
                }
            }
        }

        public void guardarCosto(string cuenta, int costo)
        {
            try
            {
                using (var client = new WebClient())
                {
                    var values = new NameValueCollection();
                    values["cuenta"] = cuenta;
                    values["costo"] = costo.ToString();

                    var response = client.UploadValues("http://192.168.1.7:5000/Costo", values);
                    var responseString = Encoding.Default.GetString(response);

                    if (responseString != "True")
                    {
                        HttpContext.Current.Response.Write("<script>window.alert('Error al guardar AVL Costos');</script>");

                    }




                }

            }
            catch
            {
                HttpContext.Current.Response.Write("<script>window.alert('Problema con la peticion avl');</script>");
            }
        }

        public void guardarBitacora(string usuario, string cuenta, int costo, string habitacion, string fechai, string fechaf)
        {
            try
            {
                using (var client = new WebClient())
                {
                    var values = new NameValueCollection();
                    values["usuario"] = usuario;
                    values["cuenta"] = cuenta;
                    values["costo"] = costo.ToString();
                    values["habitacion"] = habitacion;
                    values["fechai"] = fechai;
                    values["fechaf"] = fechaf;

                    var response = client.UploadValues("http://192.168.1.7:5000/Bitacora", values);
                    var responseString = Encoding.Default.GetString(response);

                    if (responseString != "True")
                    {
                        HttpContext.Current.Response.Write("<script>window.alert('Error al guardar arbol B Bitacora');</script>");

                    }




                }

            }
            catch
            {
                HttpContext.Current.Response.Write("<script>window.alert('Problema con la peticion arbol B');</script>");
            }
        }

        public void guardarDispersa(string mes, string year, string dia,string usuario, string cuenta, string habitacion)
        {
            try
            {
                using (var client = new WebClient())
                {

                    
                    var values = new NameValueCollection();
                    values["mes"] = mes;
                    values["year"] = year;
                    values["dia"] = dia;
                    values["usuario"] = usuario;
                    values["habitacion"] = habitacion;
                    values["tarjeta"] = cuenta;

                    var response = client.UploadValues("http://192.168.1.7:5000/Dispersa", values);
                    var responseString = Encoding.Default.GetString(response);

                    if (responseString != "True")
                    {
                        HttpContext.Current.Response.Write("<script>window.alert('Error al guardar Dispersa');</script>");

                    }




                }

            }
            catch
            {
                HttpContext.Current.Response.Write("<script>window.alert('Problema con la peticion Dispersa');</script>");
            }
        }

        protected void Button3_Click(object sender, EventArgs e)
        {

        }
    }
}