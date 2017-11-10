package com.example.equipo.ellobo;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class organizar extends AppCompatActivity {
    Button btusuarios, bthabitacion,btreservacion;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_organizar);
        btusuarios=  (Button) findViewById(R.id.button1);
        bthabitacion= (Button) findViewById(R.id.button2);
        btreservacion=(Button) findViewById(R.id.button3);

        btusuarios.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent siguiente = new Intent(organizar.this,RegistrarUsuarios.class);
                startActivity(siguiente);
            }


        });

        bthabitacion.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent siguiente = new Intent(organizar.this,Agregar_Habitacion.class);
                startActivity(siguiente);
            }
        });

        btreservacion.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent siguiente = new Intent(organizar.this,Reservaciones.class);
                startActivity(siguiente);
            }
        });
    }
}
