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
    public partial class Registrarse : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {

            if (TextBox1.Text.Length < 4)
            {
                HttpContext.Current.Response.Write("<script>window.alert('Se necesita contraseña mayor de 4 digitos');</script>");
            }
            else
            {
                registrar(TextBox1.Text, TextBox2.Text, TextBox3.Text, TextBox4.Text, TextBox5.Text);
            }
        }
        public void registrar(string user, string password, string direccion, string telefono, string edad)
        {
            try
            {
                using (var client = new WebClient())
                {
                    var values = new NameValueCollection();
                    values["usuario"] = user;
                    values["contra"] = password;
                    values["direccion"] = direccion;
                    values["telefono"] = telefono;
                    values["edad"] = edad;


                    var response = client.UploadValues("http://192.168.1.7:5000/Usuario", values);
                    var responseString = Encoding.Default.GetString(response);

                    if (responseString.Equals("True"))
                    {
                        HttpContext.Current.Response.Write("<script>window.alert('Usuario Registrado con Exito');</script>");
                    }
                    else
                    {
                        HttpContext.Current.Response.Write("<script>window.alert('Error al Registrar');</script>");
                    }



                }

            }
            catch
            {
                HttpContext.Current.Response.Write("<script>window.alert('Problema con la peticion');</script>");
            }
        }

        protected void Button2_Click(object sender, EventArgs e)
        {
            TextBox6.Text = "";
            if (FileUploadControl.HasFile)
            {
                try
                {
                    string filename = Path.GetFileName(FileUploadControl.FileName);
                    FileUploadControl.SaveAs(Server.MapPath("~/") + filename);

                    StreamReader sr = new StreamReader(Server.MapPath("~/") + filename);
                    string contenido = sr.ReadToEnd();
                    sr.Close();
                   TextBox6.Text = contenido;
                    string nombre = "";
                    string contraseña = "";
                    string direccion = "";
                    string telefono = "";
                    string edad = "";
                    Boolean check = false;
                    XmlDocument myXmlDocument = new XmlDocument();
                    myXmlDocument.Load(Server.MapPath("~/") + filename);


                    XmlNode node = myXmlDocument.DocumentElement;

                    foreach (XmlNode node1 in node.ChildNodes)

                        if (node1.Name == "usuario")
                        {

                            nombre = node1.FirstChild.InnerText;
                            contraseña = node1.FirstChild.NextSibling.InnerText;
                            direccion = node1.FirstChild.NextSibling.NextSibling.InnerText;
                            telefono = node1.FirstChild.NextSibling.NextSibling.NextSibling.InnerText;
                            edad = node1.LastChild.InnerText;

                            if (contraseña.Length < 4)
                            {
                                check = true;
                            }
                           

                            //TextBox6.Text += nombre + " " + contraseña + " " + direccion + " " + telefono + " " + edad + "\n";
                            
                        }
                    foreach (XmlNode node1 in node.ChildNodes) 

                        if (node1.Name == "usuario")
                        {

                            nombre = node1.FirstChild.InnerText;
                            contraseña = node1.FirstChild.NextSibling.InnerText;
                            direccion = node1.FirstChild.NextSibling.NextSibling.InnerText;
                            telefono = node1.FirstChild.NextSibling.NextSibling.NextSibling.InnerText;
                            edad = node1.LastChild.InnerText;

                            if (check == true)
                            {
                                HttpContext.Current.Response.Write("<script>window.alert('Alguna Contraseña incorrecta en el documento');</script>");
                            }
                            else
                            {


                                //TextBox6.Text += nombre + " " + contraseña + " " + direccion + " " + telefono + " " + edad + "\n";
                                guardar(nombre, contraseña, direccion, telefono, edad);
                                HttpContext.Current.Response.Write("<script>window.alert('Usuarios Guardados');</script>");
                            }
                        }

                  


                }
                catch (Exception ex)
                {
                    HttpContext.Current.Response.Write("<script>window.alert('Error al subir archivo');</script>");
                }
            }


        }

        public void guardar(string nombre, string contraseña,string direccion, string telefono, string edad)
        {
            try
            {
                using (var client = new WebClient())
                {
                    var values = new NameValueCollection();
                    values["usuario"] = nombre;
                    values["contra"] = contraseña;
                    values["direccion"] = direccion;
                    values["telefono"] = telefono;
                    values["edad"] = edad;

                    var response = client.UploadValues("http://192.168.1.7:5000/Usuario", values);
                    var responseString = Encoding.Default.GetString(response);

                    if (responseString != "True")
                    {
                        HttpContext.Current.Response.Write("<script>window.alert('Error al guardar los usuarios');</script>");

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