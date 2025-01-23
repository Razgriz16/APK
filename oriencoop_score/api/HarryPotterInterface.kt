package com.example.oriencoop_score.api

import com.example.oriencoop_score.model.CharactersItem
import retrofit2.http.GET

interface HarryPotterApi {
    @GET(value = "api/characters")
    suspend fun getCharacters() : List<CharactersItem>
}