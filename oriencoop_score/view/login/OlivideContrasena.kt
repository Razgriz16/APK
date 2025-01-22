package com.example.oriencoop_score.view.login

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.oriencoop_score.R


//@Preview(showBackground = true)
@Composable
fun OlvideContrasena() {
    // States for the text fields
    var Rut by remember { mutableStateOf("") }
    var Serie by remember { mutableStateOf("") }

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.White),
        contentAlignment = Alignment.Center
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // Logo placeholder
            Image(painter = painterResource(id= R.drawable.logooriencoop), contentDescription = "Logo")
            /*Text(
                text = "Oriencoop",
                fontSize = 28.sp,
                color = Color(0xFF006FB6)
            )*/


            Spacer(modifier = Modifier.height(20.dp))

            // Card with form
            Card(
                modifier = Modifier
                    .fillMaxWidth(0.9f),
            ) {
                Column(
                    modifier = Modifier
                        .background(color = Color(0xFF006FB6))
                        .fillMaxWidth()
                        .padding(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(
                        text = "Recupere Clave",
                        fontSize = 20.sp,
                        color = Color.White
                    )

                    Spacer(modifier = Modifier.height(16.dp))

                    // Rut TextField
                    TextField(
                        value = Rut,
                        onValueChange = { Rut = it },
                        label = { Text("Rut") },
                        modifier = Modifier.fillMaxWidth()
                    )

                    Spacer(modifier = Modifier.height(8.dp))

                    // Serie TextField
                    TextField(
                        value = Serie,
                        onValueChange = { Serie = it },
                        label = { Text("Serie") },
                        modifier = Modifier.fillMaxWidth()
                    )

                    Spacer(modifier = Modifier.height(16.dp))

                    // Ingresar Button
                    Button(
                        onClick = { /* Handle login */ },
                        colors = ButtonDefaults.buttonColors(
                            containerColor = Color(0xFFf49600) // Orange color
                        ),
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        Text(text="Solicitar Clave", color = Color.White)
                    }

                    Spacer(modifier = Modifier.height(8.dp))

                    // Links
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.Center
                    ) {
                        TextButton(onClick = { /* Handle forgot Serie */ }) {
                            Text("Atrás", color = Color.White)
                        }

                    }
                }
            }
        }
    }
}
