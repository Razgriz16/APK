package com.example.oriencoop_score

import com.example.oriencoop_score.view_model.LoginViewModel
import com.example.oriencoop_score.view.PantallaPrincipal
import androidx.compose.runtime.Composable
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.oriencoop_score.view.Login
import com.example.oriencoop_score.view.HarryPotterView
import com.example.oriencoop_score.view.MisProductos
import com.example.oriencoop_score.view_model.HarryPotterViewModel
import com.example.oriencoop_score.view_model.PantallaPrincipalViewModel
import com.example.oriencoop_score.view_model.TestViewModel

@Composable
fun Navigation() {
    val navController = rememberNavController()
    NavHost(navController = navController, startDestination = Pantalla.Login.route) {
        composable(route = Pantalla.Login.route) {
            Login(navController = navController, viewModel = LoginViewModel())
        }

        composable(route = Pantalla.MisProductos.route) {
            MisProductos(navController = navController)
        }

        composable(route = Pantalla.PantallaPrincipal.route) {
            PantallaPrincipal(navController = navController, viewModel = PantallaPrincipalViewModel())
        }

        composable(route = Pantalla.HarryPotterView.route) {
            val harryPotterViewModel: HarryPotterViewModel = viewModel()
            HarryPotterView(navController = navController, viewModel = harryPotterViewModel)
        }

    }
}


