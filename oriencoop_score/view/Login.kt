package com.example.oriencoop_score.view

import com.example.oriencoop_score.view_model.LoginViewModel
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.livedata.observeAsState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import com.example.oriencoop_score.Pantalla

import com.example.oriencoop_score.R
import kotlinx.coroutines.launch

@Composable
fun Login(navController: NavController, viewModel: LoginViewModel) {

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.White),
        contentAlignment = Alignment.Center
    ) { LoginScreen(navController, viewModel) }
}
//@Preview
@Composable
fun LoginScreen(navController: NavController, viewModel: LoginViewModel) {
    val rut : String by viewModel.rut.observeAsState(initial = "");
    val password : String by viewModel.password.observeAsState(initial = "");
    val loginEnable: Boolean by viewModel.loginEnable.observeAsState(initial = false);
    val isLoading: Boolean by viewModel.isLoading.observeAsState(initial = false);
    val coroutineScope = rememberCoroutineScope()

        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(10.dp)
                .imePadding(),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // Logo
            Image(painter = painterResource(id= R.drawable.logooriencoop), contentDescription = "Logo")
            /*Text(
                text = "Oriencoop",
                fontSize = 28.sp,
                color = Color(0xFF006FB6)
            )*/


            Spacer(modifier = Modifier.height(5.dp))

            // Card with form
            Card(
                modifier = Modifier
                    .fillMaxWidth(0.9f),

            ) {

                // Cuadro azul de iniciar sesión
                Column(
                    modifier = Modifier
                        .background(color = Color(0xFF006FB6))
                        .fillMaxWidth()
                        .padding(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(
                        text = "Inicia sesión",
                        fontSize = 20.sp,
                        color = Color.White
                    )

                    Spacer(modifier = Modifier.height(16.dp))

                    // RUT TextField
                    TextField(
                        value = rut,
                        onValueChange = { viewModel.onLoginChanged(it, password) },
                        label = { Text("RUT") },
                        modifier = Modifier.fillMaxWidth()

                    )

                    Spacer(modifier = Modifier.height(8.dp))

                    // Password TextField
                    TextField(
                        value = password,
                        onValueChange = { viewModel.onLoginChanged(rut, it) },
                        label = { Text("Contraseña") },
                        visualTransformation = PasswordVisualTransformation(),
                        modifier = Modifier.fillMaxWidth()
                    )

                    Spacer(modifier = Modifier.height(16.dp))

                    // Ingresar Button
                    Button(
                        onClick = {navController.navigate(Pantalla.PantallaPrincipal.route); coroutineScope.launch { viewModel.onLoginSelected() }},
                        colors = ButtonDefaults.buttonColors(
                            containerColor = Color(0xFFf49600), // Orange color
                            //disabledContentColor = Color(0xFFf49600)
                        ),
                        //######################################enabled = loginEnable,
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        Text(text = "Ingresar", color = Color.White)
                    }

                    Spacer(modifier = Modifier.height(8.dp))

                    // Links
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween
                    ) {
                        TextButton(onClick = { /* Handle forgot password */ }) {
                            Text("¿Olvidaste tu clave?", color = Color.White)
                        }

                        TextButton(onClick = { /* Handle create password */ }) {
                            Text("Crear clave", color = Color.White)
                        }
                    }
                }
            }
        }
    }

