/**
 * Generic Admin on rest Custom Fields!
 * Change/add at your own risk! 
**/
import React from 'react';
import PropTypes from 'prop-types';
import {
    TextField
} from 'admin-on-rest';

const objectToText = ModifiedComponent => props => {
    let data = props.record[props.source];
    props.record[props.source] = data instanceof Object ? JSON.stringify(data) : data;   
    return <ModifiedComponent {...props} addLabel />;
}

export const ObjectField = objectToText(TextField);
/* End of Generic authClient.js */