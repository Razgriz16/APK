package com.example.oriencoop_score.view.main

import androidx.compose.foundation.content.MediaType.Companion.Text
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.input.KeyboardType.Companion.Text
import androidx.lifecycle.ViewModel
import androidx.navigation.NavController
import com.example.oriencoop_score.view_model.HarryPotterViewModel

@Composable
fun HarryPotterView(navController: NavController, viewModel: HarryPotterViewModel) {
    val characters by viewModel.characters.collectAsState()

    LaunchedEffect(Unit) {
        viewModel.fetchCharacters() // Fetches characters when the screen is first displayed
    }

    if (characters.isEmpty()) {
        // Show a loading or empty state
        Text(text = "Loading...", color = Color.Black)
    } else {
        LazyColumn {
            items(characters) { character ->
                Text(text = character.name, color = Color.Black)
                Text(text = character.patronus, color = Color.Red)

            }
        }
    }
}
