import React from 'react';
import SubmissionTable from './SubmissionTable';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import IconButton from '@material-ui/core/IconButton';
import SearchIcon from '@material-ui/icons/Search';
import Typography from '@material-ui/core/Typography';

function Detective({
    query,
    submissions,
    onQueryUpdate, 
    onSubmit
}) {

  const SearchButton = () => (
    <IconButton
        onClick={onSubmit}
    >
      <SearchIcon />
    </IconButton>
    )
  
  return (
    <div>     
        <Grid container spacing={3}>
            <Grid item xs={6}>
                <Typography variant="h3">
                🧬 DNA Detective🕵
                </Typography>
            </Grid>
            <Grid item xs={6}>
                 <TextField
                    fullWidth
                    id="standard-name"
                    label="Sequence"
                    value={query}
                    onChange={onQueryUpdate}
                    variant="outlined"
                    multiline
                    rowsMax={2}
                    InputProps={{endAdornment: <SearchButton />}}
                />
            </Grid>
            <Grid item xs={12}>
                <SubmissionTable
                    submissions={submissions}
                ></SubmissionTable>
            </Grid>
        </Grid>
    </div>
  );
}

export default Detective;
