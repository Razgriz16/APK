package com.example.oriencoop_score.view.mis_productos.cuenta_cap.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.oriencoop_score.R


@Composable
fun Movimientos(
    description: String,
    date: String,
    amount: String,
    isPositive: Boolean,
    modifier: Modifier = Modifier
) {
    Row(
        modifier = modifier
            .fillMaxWidth()
            .padding(vertical = 8.dp),
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.SpaceBetween
    ) {

        Row (verticalAlignment = Alignment.CenterVertically) {
            Text(text = description,
                fontWeight = FontWeight.Bold
            )

            Spacer(modifier = Modifier.height(4.dp))

            Text(text = date,
                color = Color.Gray)
        }


        Row(verticalAlignment = Alignment.CenterVertically){
            Text(
                text = amount,
                color = if(isPositive) Color.Green else Color.Red
            )

            Icon(
                painter = painterResource(id = R.drawable.pathplus),
                contentDescription = "more",
                tint = Color.Gray
            )
        }
    }
}