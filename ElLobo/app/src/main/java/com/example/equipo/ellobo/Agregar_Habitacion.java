package com.example.equipo.ellobo;

import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
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

public class Agregar_Habitacion extends AppCompatActivity {
    EditText et1 ,et2;
    Button btCrear, btRegresar;
    final Context context = this;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_agregar__habitacion);
        btCrear = (Button) findViewById(R.id.button1);
        btRegresar=(Button) findViewById(R.id.button2);
        et1 = (EditText) findViewById(R.id.editText1);
        et2 = (EditText) findViewById(R.id.editText2);
        btCrear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String nivel = et1.getText().toString();
                String numero = et2.getText().toString();
                new FeedTask().execute(nivel,numero);
            }


        });
        btRegresar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent regresar = new Intent(Agregar_Habitacion.this,MainActivity.class);
                startActivity(regresar);
            }
        });



    }
    public class FeedTask extends AsyncTask<String, String, String> {

        @Override
        protected String doInBackground(String... params) {
            try {
                OkHttpClient client = new OkHttpClient();

                String nivel = params[0];
                String numero = params[1];


                RequestBody postData = new FormBody.Builder()
                        .add("nivel", nivel)
                        .add("numero", numero)
                        .build();

                Request request = new Request.Builder()
                        //.url("http://josecarlosing10.pythonanywhere.com/Usuario")
                        .url("http://192.168.1.7:5000/Habitacion")
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

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);

            AlertDialog.Builder builder = new AlertDialog.Builder(context)
                    .setTitle("Listo")

                    .setMessage("Habitacion Guardada")
                    .setPositiveButton("Ok", null);

            AlertDialog build = builder.create();
            build.show();

        }
    }
}
