package com.example.oriencoop_score.api


import com.example.oriencoop_score.model.UserResponse
import com.example.oriencoop_score.model.UserResponseWrapper
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

interface UserService {
    @GET("AKfycbyp9E08A93-6nVg9gjqg8S_3pY3WGD06n-QrseKmsl8WwawX3Bp8KVuNiXNMe2IalmD/exec")
    suspend fun getUsers(): Response<UserResponseWrapper>

    @POST("AKfycbyp9E08A93-6nVg9gjqg8S_3pY3WGD06n-QrseKmsl8WwawX3Bp8KVuNiXNMe2IalmD/exec")
    suspend fun validateLogin(@Body loginRequest: UserResponse): Response<UserResponseWrapper>
}






