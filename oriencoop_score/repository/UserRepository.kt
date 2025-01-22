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
    private val userService = ManageApi.userService

    suspend fun getAllUsers(): Result<List<UserResponse>> {
        return withContext(Dispatchers.IO) {
            try {
                Log.d("API Call", "Attempting to fetch users")
                val response = userService.getUsers()
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
}

