package com.example.oriencoop_score.api

import com.example.oriencoop_score.model.TestModel
import com.example.oriencoop_score.model.UserResponse
import com.example.oriencoop_score.model.UserResponseWrapper
import okhttp3.ResponseBody
import retrofit2.Call
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.POST
import retrofit2.http.PUT

interface TestApi {
    @PUT("cobranza/usuarios/login")
    suspend fun testeo(@Body testModel: TestModel): Response<ResponseBody>
}