package com.example.oriencoop_score.api

import com.example.oriencoop_score.model.HiddenLoginRequest
import com.example.oriencoop_score.model.HiddenLoginResponse
import com.example.oriencoop_score.model.ProtectedResourceResponse
import com.example.oriencoop_score.model.UserLoginRequest
import com.example.oriencoop_score.model.UserLoginResponse
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.Header
import retrofit2.http.POST
import retrofit2.http.Query

interface LoginService {
    @POST("/hidden_login")
    suspend fun hiddenLogin(@Body credentials: HiddenLoginRequest): Response<HiddenLoginResponse>

    @POST("/login")
    suspend fun userLogin(@Body credentials: UserLoginRequest): Response<UserLoginResponse>

    @GET("/protected")
    suspend fun getProtectedResource(
        @Header("Authorization") token: String,
        @Query("rut") rut: String
    ): Response<ProtectedResourceResponse>
}
