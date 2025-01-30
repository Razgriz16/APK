package com.example.oriencoop_score.view

import MindicatorsViewModel
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.livedata.observeAsState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Alignment.Companion.Center
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.oriencoop_score.Pantalla
import com.example.oriencoop_score.R
import com.example.oriencoop_score.Result
import com.example.oriencoop_score.model.Indicador
import com.example.oriencoop_score.ui.theme.AppTheme

// Función trata la fila superior de la app
@Composable
fun HeaderRow(
    onMenuClick: () -> Unit = {},
    onLogoClick: () -> Unit = {},
    onAlertClick: () -> Unit = {}
) {
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
                .clickable { onMenuClick() }
        )
        Image(
            painter = painterResource(id = R.drawable.logooriencoop),
            contentDescription = null,
            modifier = Modifier
                .size(120.dp)
                .clickable { onLogoClick() }
        )
        Image(
            painter = painterResource(id = R.drawable.icon_alert_bellicon_top),
            contentDescription = null,
            modifier = Modifier
                .size(60.dp)
                .padding(end = 25.dp)
                .clickable {onAlertClick() }
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
fun Saldo() {

    Box(
        modifier = Modifier
            .padding(top = 40.dp, start = 40.dp, end = 40.dp)
            .height(65.dp)
            .width(300.dp)
            //.background(color = Color.Blue)
            .shadow(shape = RectangleShape, elevation = 2.dp)
    ) { }
}

@Composable
fun UltimosMov() {
    Box(
        modifier = Modifier
            .padding(5.dp)
            .height(25.dp)
            .width(300.dp)
            .shadow(
                shape = RectangleShape,
                elevation = 2.dp
            )
    ) {/* agregar contenido acá*/ }
}

//*****Barra inferior de la app*****
@Composable
fun BottomBar(navController: NavController) {
    Row(
        modifier = Modifier

            .fillMaxWidth()
            .height(80.dp)
            .padding(top = 15.dp)
            .background(Color.White),
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.SpaceBetween,
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
                .clickable { navController.navigate(Pantalla.MisProductos.route) }
        )

        // Giro
        Image(
            painter = painterResource(id = R.drawable.icon_arrow_undoicons),
            contentDescription = null,
            modifier = Modifier
                .size(60.dp)
                .padding(start = 25.dp)
                .clickable { }
        )

        // Pago

        Image(
            painter = painterResource(id = R.drawable.icon_sign_dollaricons),
            contentDescription = null,

            modifier = Modifier
                .size(60.dp)
                .padding(end = 25.dp)
                .clickable { }
        )

    }
}

@Composable
fun MindicatorTest(mindicator: MindicatorsViewModel){
    // Observe the LiveData as Compose state
    val indicadoresState by mindicator.indicadores.observeAsState()
    val isLoading by mindicator.isLoading.observeAsState(false)

    // Display loading state
    if (isLoading) {
        LoadingScreen()
    } else {
        // Display the data
        when (val result = indicadoresState) {
            is Result.Success -> {
                val uf = mindicator.getUF()
                val dolar = mindicator.getDolar()
                val euro = mindicator.getEuro()
                val utm = mindicator.getUTM()

                StructuredLayout(uf, dolar, euro, utm)

            }
            is Result.Error -> {
                Text(text = "Error: ${result.exception.message}")
            }
            else -> {
                // Handle other states (e.g., loading or initial state)
            }
        }
    }
}

@Composable
fun StructuredLayout(uf: String?, dolar: String?, euro: String?, utm: String?) {
    Column (modifier = Modifier.padding(horizontal = 60.dp)){
        Text(modifier= Modifier.fillMaxWidth(), text = "Indicadores Económicos", style = AppTheme.typography.titulos, color = AppTheme.colors.azul, textAlign = TextAlign.Center)
        Spacer(modifier = Modifier.height(16.dp))

        // First row: UF and Dolar
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween
        ) {

            Text(text = "UF: $uf", style = AppTheme.typography.normal)
            Text(text = "Dolar: $dolar", style = AppTheme.typography.normal)
        }

        // Second row: Euro and UTM
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Text(text = "Euro: $euro", style = AppTheme.typography.normal)
            Text(text = "UTM: $utm", style = AppTheme.typography.normal )
        }
    }
}

@Composable
fun ErrorScreen(exception: Throwable) {
    Box(
        contentAlignment = Center,
        modifier = Modifier.fillMaxSize()
    ) {
        Text(text = "Error: ${exception.message}", color = Color.Red)
    }
}

@Composable
fun LoadingScreen() {
    Box(
        contentAlignment = Center,
        modifier = Modifier.fillMaxSize()
    ) {
        CircularProgressIndicator()
    }
}
/*
@Composable
fun MindicatorsScreen(viewModel: MindicatorsViewModel) {
    // Observe the LiveData as Compose state
    val indicadoresState by viewModel.indicadores.observeAsState()
    val isLoading by viewModel.isLoading.observeAsState(false)

    // Handle loading state
    if (isLoading) {
        LoadingScreen()
    } else {
        // Handle the result state
        when (val result = indicadoresState) {
            is Result.Success -> {
                val indicador = result.data
                SuccessScreen(indicador)

            }
            is Result.Error -> {
                ErrorScreen(result.exception)
            }
            else -> {
                // Initial state or loading
            }
        }
    }
}
*/

/*
@Composable
fun SuccessScreen(indicador: Indicador) {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(text = "Dolar: ${indicador.Dolar}", style = AppTheme.typography.normal)
        Text(text = "Euro: ${indicador.Euro}", style = AppTheme.typography.normal)
        Text(text = "UF: ${indicador.UF}", style = AppTheme.typography.normal)
        Text(text = "U.T.M: ${indicador.UTM}", style = AppTheme.typography.normal)

    }
}
 */







