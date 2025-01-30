package com.example.oriencoop_score.repository

import android.util.Log
import com.example.oriencoop_score.api.LoginManageApi
import com.example.oriencoop_score.api.LoginManageApi.loginService
import com.example.oriencoop_score.api.LoginService

import com.example.oriencoop_score.model.HiddenLoginRequest
import com.example.oriencoop_score.model.HiddenLoginResponse
import com.example.oriencoop_score.model.ProtectedResourceResponse
import com.example.oriencoop_score.model.UserLoginRequest
import com.example.oriencoop_score.model.UserLoginResponse
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import retrofit2.Response
import com.example.oriencoop_score.Result
import java.io.IOException


class LoginRepository {
    private val loginService = LoginManageApi.loginService

    suspend fun performHiddenLogin(
        username: String,
        password: String
    ): Result<HiddenLoginResponse> {
        return withContext(Dispatchers.IO) {
            try {
                val response = loginService.hiddenLogin(HiddenLoginRequest(username, password))
                if (response.isSuccessful) {
                    val data = response.body()
                    if (data != null) {
                        Log.d("Login", "Hidden login successful: ${data.token}")
                        Result.Success(data)
                    } else {
                        Log.e("LoginError", "Response body is null")
                        Result.Error(Exception("Response body is null"))
                    }
                } else {
                    Log.e("LoginError", "Hidden login failed: ${response.code()} - ${response.errorBody()?.string()}")
                    throw Exception("Hidden login failed")
                }
            } catch (e: IOException) {
                Log.e("Retrofit", "Network error: ${e.message}")
                Result.Error(e)
            }

        }
    }

    suspend fun performUserLogin(
        rut: String,
        password: String,
        token: String
    ): Result<UserLoginResponse> {
        return withContext(Dispatchers.IO) {
            val response = loginService.userLogin(UserLoginRequest(rut, password, token))
            try {
                if (response.isSuccessful) {
                    val data = response.body()
                    if (data != null) {
                        Log.d("Api call exitosa ${data.rut}", "mensaje:${data.message}")
                        Result.Success(data)
                    } else {
                        Result.Error(Exception("Response body is null"))
                    }
                } else {
                    throw Exception("Hidden login failed")
                }
            } catch (e: IOException) {
                Log.e("Retrofit", "Network error: ${e.message}")
                Result.Error(e)
            }
        }
    }

    suspend fun fetchProtectedResource(
        token: String,
        rut: String
    ): Result<ProtectedResourceResponse> {
        return withContext(Dispatchers.IO) {

            try {
                val response = loginService.getProtectedResource(token, rut)
                if (response.isSuccessful){
                    val data = response.body()
                    if (data!=null){
                        Log.d("Api call exitosa ", "mensaje: ${data.message}")
                        Result.Success(data)
                    } else {
                        Result.Error(Exception("Response body is null"))
                    }
                } else {
                    throw Exception("Hidden login failed")
                }

            }catch (e: IOException) {
                Log.e("Retrofit", "Network error: ${e.message}")
                Result.Error(e)
            }

        }

    }
}