import React from "react";
import { MuiThemeProvider } from "@material-ui/core";
import { theme } from "themes/theme";

import { Provider as AuthProvider } from "contexts/AuthContext";
import { Provider as MealProvider } from "contexts/MealContext";
import { Provider as AlertProvider } from "contexts/AlertContext";

import "App.css";
const RootProvider = ({ children }) => {
  return (
    <MuiThemeProvider theme={theme}>
      <AlertProvider>
        <AuthProvider>
          <MealProvider>{children}</MealProvider>
        </AuthProvider>
      </AlertProvider>
    </MuiThemeProvider>
  );
};

export default RootProvider;
