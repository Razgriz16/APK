package com.example.oriencoop_score.view.mis_productos.cuenta_cap.components


import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.navigation.compose.rememberNavController
import com.example.oriencoop_score.R


@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun Detalles(
    accountNumber: String,
    balance: String,
    openingDate: String,
    accountType: String,
    modifier: Modifier = Modifier
) {
    Card(
        modifier = modifier.fillMaxWidth(),
        colors = CardDefaults.cardColors(containerColor = Color(0xFF2477C3))
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween,
                modifier = Modifier.fillMaxWidth()
            ) {
                // Número de cuenta
                Text(modifier = Modifier.fillMaxWidth(),
                    textAlign = TextAlign.Center,
                    text = accountNumber,
                    style = com.example.oriencoop_score.ui.theme.AppTheme.typography.normal,
                    color = Color.White,
                    fontWeight = FontWeight.Bold
                )

                Icon(
                    painter = painterResource(id = R.drawable.info),
                    contentDescription = "Info",
                    tint = com.example.oriencoop_score.ui.theme.AppTheme.colors.amarillo,
                    modifier = Modifier.clickable{}.size(24.dp)
                )
            }

            Spacer(modifier = Modifier.height(8.dp))

            // Saldo
            Row(modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween) {
                Text(
                    text = "Saldo Contble",
                    color = Color.White,
                    style = com.example.oriencoop_score.ui.theme.AppTheme.typography.normal
                )
                Text(
                    text = balance,
                    color = Color.White,
                    style = com.example.oriencoop_score.ui.theme.AppTheme.typography.normal,
                    fontWeight = FontWeight.Bold
                )
            }

            Spacer(modifier = Modifier.height(4.dp))
            Row(modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween) {
                Text(
                    text = "Fecha Apertura",
                    color = Color.White,
                    style = com.example.oriencoop_score.ui.theme.AppTheme.typography.normal

                )
                Text(
                    text = openingDate,
                    color = Color.White,
                    style = com.example.oriencoop_score.ui.theme.AppTheme.typography.normal

                )
            }

            Spacer(modifier = Modifier.height(4.dp))
            Row(modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween) {
                Text(
                    text = "Tipo",
                    color = Color.White,
                    style = com.example.oriencoop_score.ui.theme.AppTheme.typography.normal
                )
                Text(
                    text = accountType,
                    color = Color.White,
                    style = com.example.oriencoop_score.ui.theme.AppTheme.typography.normal
                )
            }
        }
    }
}