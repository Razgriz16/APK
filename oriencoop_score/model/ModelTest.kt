package com.example.oriencoop_score.model

import java.util.Objects

data class UserResponseWrapper(
        val data: List<UserResponse>

)

data class UserResponse(
        val rut: String,
        val password: String
)

