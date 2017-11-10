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

public class RegistrarUsuarios extends AppCompatActivity {
    EditText et1, et2, et3,et4,et5;
    Button btCrear,btRegresar;
    final Context context = this;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registrar_usuarios);
        et1 = (EditText) findViewById(R.id.editText1);
        et2 = (EditText) findViewById(R.id.editText2);
        et3 = (EditText) findViewById(R.id.editText3);
        et4 = (EditText) findViewById(R.id.editText4);
        et5 = (EditText) findViewById(R.id.editText7);

        btCrear = (Button) findViewById(R.id.button);
        btRegresar=(Button) findViewById(R.id.button4);
        btCrear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


                String usuario = et1.getText().toString();
                String contra = et2.getText().toString();
                String direccion = et3.getText().toString();
                String telefono = et4.getText().toString();
                String edad = et5.getText().toString();

                if (usuario.equals("") || contra.equals("") || direccion.equals("") || telefono.equals("") || edad.equals("") ){

                    AlertDialog.Builder builder = new AlertDialog.Builder(context)
                            .setTitle("Error")

                            .setMessage("Faltan datos")
                            .setPositiveButton("Ok", null);

                    AlertDialog build = builder.create();
                    build.show();
                }
                else if (usuario.length()<4){
                    AlertDialog.Builder builder = new AlertDialog.Builder(context)
                            .setTitle("Contraseña invalida")

                            .setMessage("Se necesita Contraseña mayor de 4 digitos")
                            .setPositiveButton("Ok", null);

                    AlertDialog build = builder.create();
                    build.show();
                }
                else {

                    String ar = direccion + "/" + telefono + "/" + edad;

                    new FeedTask().execute(usuario, contra, ar);
                }
            }


        });
        btRegresar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent regresar = new Intent(RegistrarUsuarios.this, MainActivity.class);
                startActivity(regresar);
            }
        });
    }
    public class FeedTask extends AsyncTask<String, String, String> {

        @Override
        protected String doInBackground(String... params) {
            try {
                OkHttpClient client = new OkHttpClient();

                String usuario = params[0];
                String contra = params[1];

                String ar = params[2];

                String[] substring = ar.split("/");

                String direccion = substring[0];
                String telefono = substring[1];
                String edad = substring[2];


                RequestBody postData = new FormBody.Builder()
                        .add("usuario", usuario)
                        .add("contra", contra)
                        .add("direccion", direccion)
                        .add("telefono", telefono)
                        .add("edad", edad)
                        .build();

                Request request = new Request.Builder()
                        //.url("http://josecarlosing10.pythonanywhere.com/Usuario")
                        .url("http://192.168.1.7:5000/Usuario")
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

                    .setMessage("Registro Guardado")
                    .setPositiveButton("Ok", null);

            AlertDialog build = builder.create();
            build.show();

        }
    }
}
