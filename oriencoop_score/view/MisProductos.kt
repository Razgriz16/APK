package com.example.oriencoop_score.view

import androidx.compose.ui.graphics.Path
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
import androidx.compose.ui.draw.drawBehind
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
fun MisProductos(navController: NavController) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.White)
    ) {


        Spacer(modifier = Modifier.weight(1f))

        boton(Modifier.padding(horizontal = 59.dp, vertical=146.dp))



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
@Composable
fun boton(modifier: Modifier){
    Box(
        modifier = Modifier
            .size(96.dp, 83.dp)
            .background(color = Color.Red)
            .offset(x = -50.dp, y = 50.dp)
    ){}



}



