package com.ps.assignment1q3;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ExpandableListView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MainActivity extends AppCompatActivity {
    EditText etName, etEmail, etMobile, etPassword, etAge;
    Button btnRegister;
    ExpandableListView expandableListView;
    List<String> groupList;
    Map<String, List<String>> childMap;

    List<String> userRecords;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        etName = findViewById(R.id.etName);
        etEmail = findViewById(R.id.etEmail);
        etMobile = findViewById(R.id.etMobile);
        etPassword = findViewById(R.id.etPassword);
        etAge = findViewById(R.id.etAge);
        btnRegister = findViewById(R.id.btnRegister);
        expandableListView = findViewById(R.id.records);

        groupList = new ArrayList<>();
        childMap = new HashMap<>();
        userRecords = new ArrayList<>();



        btnRegister.setOnClickListener(v -> {

            String name = etName.getText().toString();
            String email = etEmail.getText().toString();
            String mobile = etMobile.getText().toString();
            String password = etPassword.getText().toString();
            String age = etAge.getText().toString();

            if(name.isEmpty() || email.isEmpty() || mobile.isEmpty()
                    || password.isEmpty() || age.isEmpty()) {

                Toast.makeText(this,
                        "All fields required",
                        Toast.LENGTH_SHORT).show();
                return;
            }

            String record =
                    "Name: " + name +
                            "\nEmail: " + email +
                            "\nMobile: " + mobile +
                            "\nAge: " + age;

            userRecords.add(record);
            Toast.makeText(this,
                    "Registered Successfully",
                    Toast.LENGTH_SHORT).show();
            clearFields();

        });
    }

    private void clearFields() {
        etName.setText("");
        etEmail.setText("");
        etMobile.setText("");
        etPassword.setText("");
        etAge.setText("");
    }
}