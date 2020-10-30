import React, {Component} from 'react';
import axios from 'axios';
import Detective from './Detective';
import Container from '@material-ui/core/Container';

export class DetectiveContainer extends Component {

    state = {
        query: '',
        submissions: []    
    }

    handleQueryUpdate = (event) => {
        this.setState({query: event.target.value});
    }

    fetchSubmissions = () => {
        const url = `/submissions/`;
        axios.get(url)
          .then(response => {
            this.setState({submissions: response.data});
        });
    }

    submitQuery = () => {
        const url = `/submission/`;
            
        let bodyFormData = new FormData();
        bodyFormData.append('query', this.state.query);
        axios({
            method: 'post',
            url: url,
            data: bodyFormData,
            headers: {'Content-Type': 'multipart/form-data' }
        }).then(response => {
            let submission = response.data;
            if (submission.id) {
                this.setState({query: '', submissions: [submission, ...this.state.submissions]});
            }
        });
    }

    /**
     * Fetch initial data and periodically refresh to update 
     */
    componentDidMount() {
        this.fetchSubmissions();
        this.interval = setInterval(() => {
            let subs = this.state.submissions.filter(submission => submission.status === 'IN_PROGRESS')
            if (subs.length) {
                this.fetchSubmissions();
            }
          }, 5000);
    }
    
    render() {
        return (
            <Container maxWidth="lg">
                <Detective
                    query={this.state.query}
                    submissions={this.state.submissions}
                    onQueryUpdate={this.handleQueryUpdate}
                    onSubmit={this.submitQuery}
                ></Detective>
            </Container>
        )
    }

}
