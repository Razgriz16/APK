package com.example.oriencoop_score.repository

import com.example.oriencoop_score.api.TestApi
import com.example.oriencoop_score.model.TestModel

class TestRepository(private val testApi: TestApi) {

    suspend fun updateTestData(testModel: TestModel): String {
        return try {
            val response = testApi.testeo(testModel)
            if (response.isSuccessful) {
                "Update successful!"
            } else {
                "Update failed: ${response.errorBody()?.string()}"
            }
        } catch (e: Exception) {
            "Error: ${e.message}"
        }
    }
}