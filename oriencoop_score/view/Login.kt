package com.example.oriencoop_score.view
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import com.example.oriencoop_score.view_model.LoginViewModel
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import com.example.oriencoop_score.LoginState
import com.example.oriencoop_score.Pantalla
import com.example.oriencoop_score.R
import com.example.oriencoop_score.Result
import com.example.oriencoop_score.model.HiddenLoginResponse
import com.example.oriencoop_score.model.ProtectedResourceResponse
import com.example.oriencoop_score.model.UserLoginResponse
import com.example.oriencoop_score.repository.LoginRepository
import com.example.oriencoop_score.ui.theme.AppTheme

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
        Image(painter = painterResource(id = R.drawable.logooriencoop), contentDescription = "Logo")

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

                /***************************************************************/
                // Collect the login state from the ViewModel
                val loginState by viewModel.loginState.collectAsState()

                // State for user input
                var username by remember { mutableStateOf("") }
                var password by remember { mutableStateOf("") }

                Column(
                    modifier = Modifier

                        .padding(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally,
                    verticalArrangement = Arrangement.Center
                ) {
                    // Username TextField
                    TextField(
                        value = username,
                        onValueChange = { username = it },
                        label = { Text("Username") },
                        modifier = Modifier.fillMaxWidth()
                    )

                    Spacer(modifier = Modifier.height(16.dp))

                    // Password TextField
                    TextField(
                        value = password,
                        onValueChange = { password = it },
                        label = { Text("Password") },
                        visualTransformation = PasswordVisualTransformation(),
                        modifier = Modifier.fillMaxWidth()
                    )

                    Spacer(modifier = Modifier.height(16.dp))

                    // Login Button
                    Button(

                        onClick = {viewModel.performLogin(username, password)},
                        enabled = loginState !is LoginState.Loading,
                        colors = ButtonDefaults.buttonColors(
                            containerColor = Color(0xFFf49600))

                    ) {
                        Text("Log In")
                    }

                    Spacer(modifier = Modifier.height(16.dp))

                    // Display the login state
                    when (loginState) {
                        is LoginState.Loading -> CircularProgressIndicator()
                        is LoginState.Success -> navController.navigate(Pantalla.PantallaPrincipal.route)
                        is LoginState.Error -> Text(
                            text = "error",
                            color = Color.Red
                        )

                        else -> {}
                    }
                }
            }
        }
    }
}

