package com.example.oriencoop_score.api

import com.example.oriencoop_score.model.CharactersItem
import com.example.oriencoop_score.model.UserResponse
import com.example.oriencoop_score.model.UserResponseWrapper
import retrofit2.Response
import retrofit2.http.GET

interface UserService {
    @GET("AKfycbwsL6bsza7ZmLwAnKIr1-7L4pAyUATx_JY5o3-OcsYQ_Xhz0Xe_G7eOKxu64FgHxoqG/exec")
    suspend fun getUsers(): Response<UserResponseWrapper>
}

interface HarryPotterApi {
    @GET(value = "api/characters")
    suspend fun getCharacters() : List<CharactersItem>
}