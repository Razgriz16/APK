package com.example.oriencoop_score.view_model

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.oriencoop_score.api.TestManageApi
import com.example.oriencoop_score.model.TestModel
import kotlinx.coroutines.launch
import com.example.oriencoop_score.Result
import com.example.oriencoop_score.api.TestManageApi.testApi

class TestViewModel : ViewModel() {
    private val _response = MutableLiveData<String>()
    val response: LiveData<String> get() = _response

    fun updateTestData(testModel: TestModel) {
        viewModelScope.launch {
            try {
                val response = testApi.testeo(testModel)
                if (response.isSuccessful) {
                    _response.value = "Update successful!"

                } else {
                    _response.value = "Update failed: ${response.errorBody()?.string()}"
                    Log.e("TestViewModel", "Update failed: ${response.errorBody()?.string()}")
                }
            } catch (e: Exception) {
                _response.value = "Error: ${e.message}"
                Log.e("TestViewModel", "Error: ${e.message}")
            }
        }
    }
}


