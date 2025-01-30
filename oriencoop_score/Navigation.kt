package com.example.oriencoop_score

import MindicatorsViewModel
import com.example.oriencoop_score.view_model.LoginViewModel
import com.example.oriencoop_score.view.PantallaPrincipal
import androidx.compose.runtime.Composable
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.oriencoop_score.api.LoginManageApi.loginService
import com.example.oriencoop_score.repository.LoginRepository
import com.example.oriencoop_score.repository.MindicatorsRepository
import com.example.oriencoop_score.view.Login
import com.example.oriencoop_score.view.MisProductos
import com.example.oriencoop_score.view.mis_productos.cuenta_cap.CuentaCap

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
            PantallaPrincipal(navController = navController, mindicatorsViewModel = MindicatorsViewModel(
                MindicatorsRepository()
            ))
        }

        composable(route = Pantalla.CuentaCap.route) {
            /*val harryPotterViewModel: HarryPotterViewModel = viewModel()*/
            CuentaCap(navController = navController, onBackClick = { navController.popBackStack() }) /*, viewModel = harryPotterViewModel*/
        }

    }
}


