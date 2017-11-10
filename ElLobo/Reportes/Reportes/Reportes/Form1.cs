using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Reportes
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Process.Start(@"C:\Users\equipo\AndroidStudioProjects\ElLobo\Python\users.png");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Process.Start(@"C:\Users\equipo\AndroidStudioProjects\ElLobo\Python\arbolB.png");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Process.Start(@"C:\Users\equipo\AndroidStudioProjects\ElLobo\Python\avl.png");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Process.Start(@"C:\Users\equipo\AndroidStudioProjects\ElLobo\Python\dispersa.png");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            String fecha = textBox1.Text;
            String[] sub = fecha.Split('/');

            try {
                String year = sub[0];
                String mes = sub[1];
                String dia = sub[2];
                graficar(year, mes, dia);
            }
            catch
            {
                MessageBox.Show("Ingreso mal la fecha");
            }
        }
        public void graficar(String year, String mes, String dia)
        {
            try
            {
                using (var client = new WebClient())
                {
                    var values = new NameValueCollection();
                    values["mes"] = mes;
                    values["year"] = year;
                    values["dia"] = dia;

                    var response = client.UploadValues("http://192.168.1.7:5000/Hash", values);
                    var responseString = Encoding.Default.GetString(response);

                    if (responseString == "False")
                    {
                        MessageBox.Show("No existe esta fecha");

                    }
                    else
                    {
                        Process.Start(@"C:\Users\equipo\AndroidStudioProjects\ElLobo\Python\Hash.png");
                        textBox1.Text = "";

                    }





                }

            }
            catch
            {
                
            }
        }
    }
}
