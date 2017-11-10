using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;
using System.Net;
using System.Text;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace ElLobo
{
    public partial class ModificarCosto : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            if ((TextBox1.Text != "") || (TextBox2.Text != "") || (TextBox3.Text != "")) {

                modificar(TextBox1.Text, TextBox2.Text, TextBox3.Text);

            }
            else
            {
                HttpContext.Current.Response.Write("<script>window.alert('Faltan Datos');</script>");
            }
        }
        public void modificar(string cuenta, string cuentanueva, string costonuevo)
        {
            try
            {
                using (var client = new WebClient())
                {
                    var values = new NameValueCollection();
                    values["cuenta"] = cuenta;
                    values["nuevacuenta"] = cuentanueva;
                    values["nuevocosto"] = costonuevo;


                    var response = client.UploadValues("http://192.168.1.7:5000/ModificarCosto", values);
                    var responseString = Encoding.Default.GetString(response);

                    if (responseString == "True")
                    {
                        HttpContext.Current.Response.Write("<script>window.alert('Registro Modificado con Exito');</script>");

                    }





                }

            }
            catch
            {
                HttpContext.Current.Response.Write("<script>window.alert('Problema con la peticion avl');</script>");
            }
        }
    }
}