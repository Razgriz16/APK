package com.example.oriencoop_score.api

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object ManageApiPotter {
    private const val BASE_URL = "https://hp-api.onrender.com/"

    val retrofit: Retrofit = Retrofit.Builder()
        .baseUrl(BASE_URL)
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    val harryPotterApi : HarryPotterApi = retrofit.create(HarryPotterApi::class.java)
}
