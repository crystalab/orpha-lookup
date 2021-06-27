import { createMuiTheme } from '@material-ui/core';
import { lightBlue, orange } from '@material-ui/core/colors';

export const defaultTheme = createMuiTheme({
  palette: {
    primary: orange,
    secondary: lightBlue,
  },
  overrides: {
    MuiChip: {
      root: {
        margin: 4,
      },
    }
  },
});
