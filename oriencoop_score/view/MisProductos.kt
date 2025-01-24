package com.example.oriencoop_score.view

import androidx.compose.ui.graphics.Path
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.AccountCircle
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.Build
import androidx.compose.material.icons.filled.Call
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.KeyboardArrowLeft
import androidx.compose.material.icons.filled.MailOutline
//import androidx.compose.foundation.layout.FlowRowScopeInstance.align
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.drawBehind
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.oriencoop_score.Pantalla
import com.example.oriencoop_score.R
import com.example.oriencoop_score.view_model.PantallaPrincipalViewModel
import com.example.oriencoop_score.Result
import androidx.compose.material.icons.filled.Place
import androidx.compose.ui.res.vectorResource
import androidx.compose.ui.unit.sp

//*****Pantalla Principal*****

@Composable
fun MisProductos(navController: NavController) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.White)
    ) {


        ProductsScreen(navController = navController, onBackClick = { navController.navigate(Pantalla.PantallaPrincipal.route) })


    }
}
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ProductsScreen(onBackClick: () -> Unit, navController: NavController) {
    Scaffold(
        topBar = {
            CenterAlignedTopAppBar(
                title = {

                    Text(
                        fontSize = 15.sp,
                        text = "Mis Productos",
                        color = Color(0xFF006FB6),
                        textAlign = TextAlign.Left

                    )
                },

                navigationIcon = {
                    IconButton(onClick = onBackClick) {
                        Icon(imageVector = Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back", tint = com.example.oriencoop_score.ui.theme.amarillo)
                    }

                },
                colors = TopAppBarDefaults.centerAlignedTopAppBarColors(
                    containerColor = Color.White
                )

            )
        },
        bottomBar = {
            Box(
            modifier = Modifier
                .padding(bottom = 16.dp)

        )
        { BottomBar(navController) }}


    ) { paddingValues ->
        Column(
            modifier = Modifier
                .background(Color.White)
                .fillMaxSize()
                .padding(paddingValues)
                .verticalScroll(rememberScrollState()),
            verticalArrangement = Arrangement.Center
        ) {

            Row (modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceEvenly){
                ProductButton(
                    icon = R.drawable.bank,
                    text = "Cuenta Capitalización",
                    onClick = { navController.navigate(Pantalla.HarryPotterView.route) }
                )

                ProductButton(
                    icon = R.drawable.piggy_bank,
                    text = "Cuenta De\nahorro",
                    onClick = { /* Handle click */ }
                )
            }


            Spacer(modifier = Modifier.height(16.dp))

            Row (modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceEvenly){
                ProductButton(
                    icon = R.drawable.credito_cuotas,
                    text = "Crédito en\ncuotas",
                    onClick = { /* Handle click */ }
                )

                ProductButton(
                    icon = R.drawable.lcc,
                    text = "Línea de crédito\nde cuotas",
                    onClick = { /* Handle click */ }
                )
            }


            Spacer(modifier = Modifier.height(16.dp))
            Row (modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceEvenly){
                ProductButton(
                    icon = R.drawable.lcr,
                    text = "Línea de crédito\nrotativa",
                    onClick = { /* Handle click */ }
                )

                ProductButton(
                    icon = R.drawable.deposito,
                    text = "Depósito a\nplazo",
                    onClick = { /* Handle click */ }
                )
            }
            Spacer(modifier = Modifier.height(16.dp))

            Row (modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.Center){
                ProductButton(
                    icon = R.drawable.call,
                    text = "Dap call",
                    onClick = { /* Handle click */ }
                )
            }





        }
    }
}




@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ProductButton(
    icon: Int,
    text: String,
    modifier: Modifier = Modifier,
    onClick: () -> Unit,
    contentColor: Color = Color.Black
) {
    Card(onClick = onClick, modifier = modifier) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            modifier = Modifier.padding(16.dp).size(80.dp)
        ) {
            Image(
                painter = painterResource(id = icon),
                contentDescription = null,
                modifier = Modifier.size(36.dp))
            Text(
                text = text,
                textAlign = TextAlign.Center,
                modifier = Modifier.padding(top = 8.dp),
                color = contentColor
            )
        }
    }
}




