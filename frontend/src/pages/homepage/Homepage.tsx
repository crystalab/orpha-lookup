import { Box } from '@material-ui/core';
import React from 'react';
import { BaseLayout } from '../../components/layouts/BaseLayout/BaseLayout';
import { observer } from 'mobx-react-lite';
import { DisorderList } from '../../components/DisorderList/DisorderList';
import { HpoLookup } from '../../components/HpoLookup/HpoLookup';

export const Homepage = observer(() => {

  return (
    <BaseLayout>
      <Box mb={2}>
        <HpoLookup />
      </Box>
      <Box mb={2}>
        <DisorderList />
      </Box>
    </BaseLayout>
  );
});
