package com.example.equipo.ellobo;

import android.content.Context;
import android.os.AsyncTask;
import android.os.StrictMode;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import okhttp3.FormBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class Reservaciones extends AppCompatActivity {
    EditText et, et1,et2,et3,et4,et5;
    Button btCrear, btRegresar;
    final Context context = this;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reservaciones);
        et = (EditText) findViewById(R.id.editText);
        et1 = (EditText) findViewById(R.id.editText1);
        et2 = (EditText) findViewById(R.id.editText2);
        et3 = (EditText) findViewById(R.id.editText3);
        et4 = (EditText) findViewById(R.id.editText4);
        et5 = (EditText) findViewById(R.id.editText5);

        btCrear = (Button) findViewById(R.id.button1);
        btRegresar=(Button) findViewById(R.id.button2);

        btCrear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String usuario = et.getText().toString();
                String tarjeta = et1.getText().toString();
                String habitacion = et2.getText().toString();
                String extras = et3.getText().toString();
                String fechai = et4.getText().toString();
                String fechaf = et5.getText().toString();
                int costo=0;
                if(usuario.equals("")|| (tarjeta.equals(""))||(habitacion.equals(""))||fechai.equals("")){

                    AlertDialog.Builder builder = new AlertDialog.Builder(context)
                            .setTitle("Error")

                            .setMessage("Faltan datos")
                            .setPositiveButton("Ok", null);

                    AlertDialog build = builder.create();
                    build.show();
                }
                else{
                    String[] subs= extras.split(",");
                    char[] hab = habitacion.toCharArray();

                    int numeropiso = Integer.parseInt (hab[0]+"");
                    int nume = Integer.parseInt(hab[1] +""+ hab[2]);

                    costo = (numeropiso * 200) + nume;

                    for (int i=0; i<subs.length;i++){
                        if (i > 2) {
                            costo += 50;
                        }
                        else
                        {
                            costo += 75;
                        }

                    }

                    AlertDialog.Builder builder = new AlertDialog.Builder(context)
                            .setTitle("Listo")

                            .setMessage(costo+"")
                            .setPositiveButton("Ok", null);

                    AlertDialog build = builder.create();
                    build.show();
                    char[] fecha = fechai.toCharArray();

                    String year = fecha[0] +"" +fecha[1] + fecha[2] + fecha[3];
                    String mes = fecha[4] +""+ fecha[5];
                    String dia = fecha[6] +""+ fecha[7];

                    String cont = dia+"/"+usuario+"/"+tarjeta+"/"+habitacion;
                    new FeedTask().execute(mes, year, cont);


                    FeedTask3 fed = new FeedTask3();
                    fed.doInBackground(tarjeta,costo);

                    FeedTask2 fod = new FeedTask2();
                    fod.doInBackground(usuario,tarjeta,costo,habitacion,fechai,fechaf);
                }
            }
        });
    }

    public class FeedTask2  {





        String doInBackground(String usuario, String tarjeta,int costo,String habitacion, String fechai, String fechaf) {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
            try {
                OkHttpClient client = new OkHttpClient();


                String a= costo+"";

                RequestBody postData = new FormBody.Builder()
                        .add("usuario", usuario)
                        .add("cuenta", tarjeta)
                        .add("costo", a)
                        .add("habitacion", habitacion)
                        .add("fechai", fechai)
                        .add("fechaf", fechaf)

                        .build();

                Request request = new Request.Builder()
                        //.url("http://josecarlosing10.pythonanywhere.com/CrearCarpeta")
                        .url("http://192.168.1.7:5000/Bitacora")
                        .post(postData)
                        .build();

                Response response = client.newCall(request).execute();
                String result = response.body().string();


                // et1.setText(result);
                return result;

            } catch (Exception e) {
                String mensaje = e.toString();


                return null;
            }

        }



    }
    public class FeedTask3  {





        String doInBackground(String tarjeta, int costo) {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
            try {
                OkHttpClient client = new OkHttpClient();

                String a= costo+"";


                RequestBody postData = new FormBody.Builder()
                        .add("cuenta", tarjeta)
                        .add("costo", a)

                        .build();

                Request request = new Request.Builder()
                        //.url("http://josecarlosing10.pythonanywhere.com/CrearCarpeta")
                        .url("http://192.168.1.7:5000/Costo")
                        .post(postData)
                        .build();

                Response response = client.newCall(request).execute();
                String result = response.body().string();


                // et1.setText(result);
                return result;

            } catch (Exception e) {
                String mensaje = e.toString();


                return null;
            }

        }



    }
    public class FeedTask extends AsyncTask<String, String, String> {

        @Override
        protected String doInBackground(String... params) {
            try {
                OkHttpClient client = new OkHttpClient();

                String mes = params[0];
                String year = params[1];

                String cont = params[2];

                String[] substring = cont.split("/");

                String dia = substring[0];
                String usuario = substring[1];
                String tarjeta = substring[2];
                String habitacion = substring[3];


                RequestBody postData = new FormBody.Builder()
                        .add("mes", mes)
                        .add("year", year)
                        .add("dia", dia)
                        .add("usuario", usuario)
                        .add("habitacion", habitacion)
                        .add("tarjeta", tarjeta)
                        .build();

                Request request = new Request.Builder()
                        //.url("http://josecarlosing10.pythonanywhere.com/Usuario")
                        .url("http://192.168.1.7:5000/Dispersa")
                        .post(postData)
                        .build();

                Response response = client.newCall(request).execute();
                String result = response.body().string();

                return result;

            } catch (Exception e) {
                String mensaje = e.toString();

                return null;
            }

        }

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);

            AlertDialog.Builder builder = new AlertDialog.Builder(context)
                    .setTitle("Listo")

                    .setMessage("Reservacion Guardada")
                    .setPositiveButton("Ok", null);

            AlertDialog build = builder.create();
            build.show();
            et.setText("");
            et1.setText("");
            et2.setText("");
            et3.setText("");
            et4.setText("");
            et5.setText("");

        }
    }
}
