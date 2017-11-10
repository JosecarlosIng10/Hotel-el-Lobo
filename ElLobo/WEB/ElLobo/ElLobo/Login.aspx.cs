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
    public partial class Login : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            check(TextBox1.Text, TextBox2.Text);
        }

        public void check(string user, string password)
        {
            try
            {
                using (var client = new WebClient())
                {
                    var values = new NameValueCollection();
                    values["usuario"] = user;
                    values["contra"] = password;

                    var response = client.UploadValues("http://192.168.1.7:5000/Check", values);
                    var responseString = Encoding.Default.GetString(response);

                    if (responseString.Equals("Si"))
                    {
                        HttpContext.Current.Response.Write("<script>window.alert('Bienvenido');</script>");
                    }
                    else
                    {
                        HttpContext.Current.Response.Write("<script>window.alert('Usuario no Registrado');</script>");
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