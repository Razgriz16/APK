package com.example.oriencoop_score.api

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object TestManageApi {
    private const val BASE_URL = "http://aplicaciones-desarrollo.oriencoop.cl/"

    val retrofit = Retrofit.Builder()
        .baseUrl(BASE_URL)
        .addConverterFactory(GsonConverterFactory.create())
        .build()


    val testApi = retrofit.create(TestApi::class.java)
}