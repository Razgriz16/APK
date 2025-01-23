package com.example.oriencoop_score.api

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.create

object ManageApi {
    private const val BASE_URL = "https://script.google.com/macros/s/"

    val retrofit: Retrofit = Retrofit.Builder()
        .baseUrl(BASE_URL)
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    val userService : UserService = retrofit.create(UserService::class.java)
}

