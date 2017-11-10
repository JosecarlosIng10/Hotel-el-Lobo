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
    public partial class EliminarCosto : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            if (TextBox1.Text != "")
            {
                eliminar(TextBox1.Text);

            }
            else
            {
                HttpContext.Current.Response.Write("<script>window.alert('Ingrese Cuenta');</script>");
            }
        }
        public void eliminar(string cuenta)
        {
            try
            {
                using (var client = new WebClient())
                {
                    var values = new NameValueCollection();
                    values["cuenta"] = cuenta;
                    

                    var response = client.UploadValues("http://192.168.1.7:5000/EliminarCosto", values);
                    var responseString = Encoding.Default.GetString(response);

                    if (responseString == "True")
                    {
                        HttpContext.Current.Response.Write("<script>window.alert('Registro Eliminado con Exito');</script>");

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