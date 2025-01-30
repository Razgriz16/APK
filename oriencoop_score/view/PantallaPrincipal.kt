package com.example.oriencoop_score.view
import MindicatorsViewModel
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.getValue
import androidx.compose.runtime.livedata.observeAsState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.oriencoop_score.Pantalla
import com.example.oriencoop_score.R
import com.example.oriencoop_score.Result
import com.example.oriencoop_score.model.Indicador
import com.example.oriencoop_score.repository.MindicatorsRepository


//*****Pantalla Principal*****
@Composable
fun PantallaPrincipal(
    navController: NavController,
    mindicatorsViewModel: MindicatorsViewModel
) {

    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.White),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {

        HeaderRow()


        // Saldo

        Saldo()

        // Ultimos movimientos
        Row(
            modifier = Modifier
                .align(alignment = Alignment.CenterHorizontally)
        )
        { UltimosMov() }

        Image(
            painter = painterResource(id = R.drawable.banner),
            contentDescription = "Banner",
            modifier = Modifier
                .padding(50.dp)
        )


        MindicatorTest(mindicatorsViewModel)

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


