import React from 'react';
import { observer } from 'mobx-react-lite';
import { Autocomplete } from '@material-ui/lab';
import { Chip, CircularProgress, TextField } from '@material-ui/core';
import { useMst } from '../../mobx/Root.store';

export const HpoLookup: React.FC = observer(() => {
  const { lookupStore } = useMst();
  const { suggestions, suggestionsLoading, searchFor, setHpos } = lookupStore;

  return (
    <Autocomplete
      multiple
      filterSelectedOptions
      getOptionLabel={(option: any) => option.name}
      renderTags={(value, getTagProps) =>
        value.map((option: any, index) => (
          <Chip
            color="default"
            label={option.name}
            size="small"
            {...getTagProps({ index })}
          />
        ))
      }
      renderInput={params => (
        <TextField
          {...params}
          label="Start entering symptom"
          variant="outlined"
          InputProps={{
            ...params.InputProps,
            endAdornment: (
              <>
                {suggestionsLoading ? <CircularProgress color="inherit" size={20} /> : null}
                {params.InputProps.endAdornment}
              </>
            ),
          }}
        />
      )}
      onInputChange={(event, newInputValue) => {
        searchFor(newInputValue);
      }}
      onChange={(event, newValue) => {
        setHpos(newValue ? newValue : []);
      }}
      getOptionSelected={(option: any, value: any) => option.id === value.id}
      options={suggestions.slice()}
      loading={suggestionsLoading}
    />
  );
});
