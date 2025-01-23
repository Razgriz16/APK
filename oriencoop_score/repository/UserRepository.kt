package com.example.oriencoop_score.repository

import android.util.Log
import com.example.oriencoop_score.api.ManageApi
import com.example.oriencoop_score.api.UserService
import com.example.oriencoop_score.model.UserResponse
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import retrofit2.Response
import com.example.oriencoop_score.Result

import com.example.oriencoop_score.model.UserResponseWrapper


class UserRepository {
    private val userService = ManageApi.userService // se declara la variable que llama a manage api para que esta haga la llamada a la api

    suspend fun getAllUsers(): Result<List<UserResponse>> {  // se usa suspend como funcion asíncrona y luego devuelve una respuesta de una clase persnoalizada esperando la estructura establecida en esta
        return withContext(Dispatchers.IO) { // usa Dispatchers.IO para hacer la llamada a la api en un hilo separado
            try {
                Log.d("API Call", "Attempting to fetch users")
                val response = userService.getUsers() // se llama a la api
                if (response.isSuccessful) {
                    val wrapper = response.body()
                    if (wrapper != null) {
                        Log.d("API Call", "Successful API call: ${wrapper.data}")
                        Result.Success(wrapper.data) // Return the list of users from the "data" field
                    } else {
                        Log.e("API Call", "API Error: Response body is null")
                        Result.Error(Exception("Response body is null"))
                    }
                } else {
                    Log.e("API Call", "API Error: ${response.code()} ${response.message()}")
                    Result.Error(Exception("Error: ${response.code()} ${response.message()}"))
                }
            } catch (e: Exception) {
                Log.e("API Call", "API call failed: ${e.message}")
                Result.Error(e)
            }
        }
    }

    // Validate login
    suspend fun validateLogin(loginRequest: UserResponse): Result<UserResponseWrapper> {
        return withContext(Dispatchers.IO) {
            try {
                val response = userService.validateLogin(loginRequest)
                if (response.isSuccessful) {
                    val wrapper = response.body()
                    if (wrapper != null) {
                        Result.Success(wrapper)
                    } else {
                        Result.Error(Exception("Response body is null"))
                    }
                } else {
                    Result.Error(Exception("Error: ${response.code()} ${response.message()}"))
                }
            } catch (e: Exception) {
                Result.Error(e)
            }
        }
    }
}

