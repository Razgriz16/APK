package com.example.oriencoop_score.repository

import com.example.oriencoop_score.api.ManageApiPotter
import com.example.oriencoop_score.model.CharactersItem

class HarryPotterRepository {
    private val apiService = ManageApiPotter.harryPotterApi

    suspend fun getCharacters(): List<CharactersItem> {
        return apiService.getCharacters()
    }
}