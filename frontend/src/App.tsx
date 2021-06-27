import React from 'react';
import { CssBaseline, MuiThemeProvider } from '@material-ui/core';
import { defaultTheme } from './theme/theme';
import { Homepage } from './pages/homepage/Homepage';
import { Provider as MobxProvider } from './mobx/Root.store';
import { setupStore } from './mobx/setupStore';

function App() {
  return (
    <MobxProvider value={setupStore()}>
      <MuiThemeProvider theme={defaultTheme}>
        <CssBaseline />
        <Homepage />
      </MuiThemeProvider>
    </MobxProvider>
  );
}

export default App;
