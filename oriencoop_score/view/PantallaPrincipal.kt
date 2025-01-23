package com.example.oriencoop_score.view

import androidx.compose.foundation.Image
    import androidx.compose.foundation.background
    import androidx.compose.foundation.clickable
    import androidx.compose.foundation.layout.*
    import androidx.compose.foundation.lazy.LazyColumn
    //import androidx.compose.foundation.layout.FlowRowScopeInstance.align
    import androidx.compose.material3.*
    import androidx.compose.runtime.*
    import androidx.compose.runtime.getValue
    import androidx.compose.ui.Alignment
    import androidx.compose.ui.Modifier
    import androidx.compose.ui.draw.shadow
    import androidx.compose.ui.graphics.Color
    import androidx.compose.ui.graphics.RectangleShape
    import androidx.compose.ui.res.painterResource
    import androidx.compose.ui.unit.dp
    import androidx.navigation.NavController
    import com.example.oriencoop_score.Pantalla
    import com.example.oriencoop_score.R
import com.example.oriencoop_score.view_model.PantallaPrincipalViewModel
import com.example.oriencoop_score.Result
    //*****Pantalla Principal*****
    @Composable
    fun PantallaPrincipal(navController: NavController, viewModel: PantallaPrincipalViewModel) {
        val users by viewModel.users.collectAsState()
        val coroutineScope = rememberCoroutineScope()

        Column(
            modifier = Modifier
                .fillMaxSize()
                .background(Color.White)
        ) {
            HeaderRow()


            // Saldo
            Row(modifier = Modifier
                .align(alignment = Alignment.CenterHorizontally)
            )
            {
                Saldo()
            }

            // Ultimos movimientos
            Row(modifier = Modifier
                .align(alignment = Alignment.CenterHorizontally)
            )
            { UltimosMov() }

            Image(
                painter = painterResource(id = R.drawable.banner),
                contentDescription = "Banner",
                modifier = Modifier
                    .padding(50.dp)
            )
            /*****##################################********/
            Button(
                onClick = { viewModel.fetchAllUsers() },
                    /*viewModel.fetchAllUsers()*/
                colors = ButtonDefaults.buttonColors(
                    containerColor = Color(0xFFf49600), // Orange color
                    //disabledContentColor = Color(0xFFf49600)
                ),
                modifier = Modifier.fillMaxWidth()
            ) {
                Text(text = "TestApi", color = Color.White)
            }

            when (val result = users) {
                is Result.Success -> {
                    // Display the data
                    val userList = result.data
                    LazyColumn {
                        items(userList.size) { index ->
                            val user = userList[index]
                            Text(text = "RUT: ${user.rut}, Password: ${user.password}", color = Color.Black)
                        }
                    }
                }
                is Result.Error -> {
                    // Show an error message
                    Text(text = "Error: ${result.exception.message}", color = Color.Red)
                }
                Result.Loading -> {
                    // Show a loading indicator
                    CircularProgressIndicator()
                }
                null -> {
                    // Initial state, perhaps show nothing or a placeholder
                }
            }



            Spacer(modifier = Modifier.weight(1f))
            // Bottom Bar
            Box(
                modifier = Modifier
                    .align(alignment = Alignment.Start)
                    .padding(bottom = 16.dp)

                    )
            { BottomBar(navController) }

        }
    }


    // Función trata la fila superior de la app
    @Composable
    fun HeaderRow() {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .height(80.dp)
                .padding(top = 30.dp)
                .background(Color.White),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Image(
                painter = painterResource(id = R.drawable.icon_button_menuicon_top),
                contentDescription = null,
                modifier = Modifier
                    .size(60.dp)
                    .padding(start = 25.dp)
                    .clickable { /* clickear algo */ }
            )
            Image(
                painter = painterResource(id = R.drawable.logooriencoop),
                contentDescription = null,
                modifier = Modifier
                    .size(120.dp)
                    .clickable { /* clickear algo */ }
            )
            Image(
                painter = painterResource(id = R.drawable.icon_alert_bellicon_top),
                contentDescription = null,
                modifier = Modifier
                    .size(60.dp)
                    .padding(end = 25.dp)
                    .clickable { /* clickear algo */ }
            )
        }
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(5.dp)
                .background(Color(0xFFf49600))
        )
    }
    // *****Saldo que se muestra*****
    @Composable
    fun Saldo(){
        Box(
            modifier = Modifier
                .padding(top = 40.dp, start = 40.dp, end = 40.dp)
                .height(65.dp)
                .width(300.dp)
                //.background(color = Color.Blue)
                .shadow( shape = RectangleShape, elevation = 2.dp)
        ) {/* agregar contenido acá*/}
    }

    @Composable
    fun UltimosMov(){
        Box(
            modifier = Modifier
                .padding(5.dp)
                .height(25.dp)
                .width(300.dp)
                //.background(color = Color.Red)
                .shadow(
                    shape = RectangleShape,
                    elevation = 2.dp


                )

        ) {/* agregar contenido acá*/}
    }

    //*****Barra inferior de la app*****
    @Composable
    fun BottomBar(navController: NavController) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .height(80.dp)
                .padding(top = 30.dp)
                .background(Color.White),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceBetween
        ) {

            // Home
            Image(
                painter = painterResource(id = R.drawable.icon_interface_homeicons),
                contentDescription = null,
                modifier = Modifier
                    .size(60.dp)
                    .padding(start = 25.dp)
                    .clickable { navController.navigate(Pantalla.PantallaPrincipal.route) }
            )

            // Menu
            Image(
                painter = painterResource(id = R.drawable.icon_button_menuicon_top),
                contentDescription = null,
                modifier = Modifier
                    .size(60.dp)
                    .padding(start = 25.dp)
                    .clickable {navController.navigate(Pantalla.MisProductos.route)}
            )

            // Giro
            Image(
                painter = painterResource(id = R.drawable.icon_arrow_undoicons),
                contentDescription = null,
                modifier = Modifier
                    .size(60.dp)
                    .padding(start = 25.dp)
                    .clickable {  navController.navigate(Pantalla.HarryPotterView.route);}
            )

            // Pago
            Image(
                painter = painterResource(id = R.drawable.icon_sign_dollaricons),
                contentDescription = null,
                modifier = Modifier
                    .size(60.dp)
                    .padding(end = 25.dp)
                    .clickable { /* clickear algo */ }
            )
        }
    }



