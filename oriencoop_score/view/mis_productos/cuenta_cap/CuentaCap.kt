package com.example.oriencoop_score.view.mis_productos.cuenta_cap


import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.ArrowDropDown
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.oriencoop_score.view.BottomBar
import com.example.oriencoop_score.view.mis_productos.cuenta_cap.components.Detalles
import com.example.oriencoop_score.view.mis_productos.cuenta_cap.components.Movimientos

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CuentaCap(navController: NavController, onBackClick: () -> Unit) {
    Scaffold(
        topBar = {
            CenterAlignedTopAppBar(
                title = {
                    Text(
                        text = "Cuenta capitalización",
                        color = Color.Black,
                        textAlign = TextAlign.Center
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
                .padding(16.dp)
                .verticalScroll(rememberScrollState())

        ) {
            Detalles(
                accountNumber = "08-001-0035123-0",
                balance = "$ 1.938",
                openingDate = "10-11-1997",
                accountType = "Capacitación Adulto"
            )

            Spacer(modifier = Modifier.height(24.dp))

            Text(
                text = "Últimos Movimientos",
                style = com.example.oriencoop_score.ui.theme.AppTheme.typography.titulos,
                modifier = Modifier.padding(bottom = 8.dp).align(alignment = Alignment.CenterHorizontally)
            )


            Movimientos(
                description = "Reaj. Pagado Csocial",
                date = "31-12-2024",
                amount = "+$126",
                isPositive = true
            )
            Movimientos(
                description = "Retiro",
                date = "26-03-2024",
                amount = "-$6000",
                isPositive = false
            )

            Movimientos(
                description = "Descripción",
                date = "fecha hora",
                amount = "-****",
                isPositive = false
            )

            Movimientos(
                description = "Descripción",
                date = "fecha hora",
                amount = "-****",
                isPositive = false
            )

            //TODO:  Add the rest of the items

            Spacer(modifier = Modifier.height(16.dp))

            Icon(
                imageVector = Icons.Filled.ArrowDropDown, // Replace with your PNG
                contentDescription = "Dropdown",
                tint = Color.Gray
            )
        }
    }
}

