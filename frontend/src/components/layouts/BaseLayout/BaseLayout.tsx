import React from 'react';
import { BaseLayoutProps } from './BaseLayout.props';
import { AppBar, Box, Toolbar, Typography } from '@material-ui/core';

export const BaseLayout: React.FC<BaseLayoutProps> = props => {
  const { children } = props;

  return (
    <>
      <AppBar position="sticky">
        <Toolbar>
          <Box mr={1}>
            <img src="/logo.png" alt="Orpha" />
          </Box>
          <Typography variant="h6">
            Orpha rare disease lookup
          </Typography>
        </Toolbar>
      </AppBar>
      <Box m={2}>
        {children}
      </Box>
    </>
  );
};
