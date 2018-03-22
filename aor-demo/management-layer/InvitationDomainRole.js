import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    NumberField,
    NumberInput,
    TextField,
    TextInput,
    DateField,
    DateInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateInvitationDomainRole = values => {
    const errors = {};
    if (!values.domain_id) {
        errors.domain_id = ["domain_id is required"];
    }
    if (!values.invitation_id) {
        errors.invitation_id = ["invitation_id is required"];
    }
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    return errors;
}

export const InvitationDomainRoleList = props => (
    <List {...props} title="InvitationDomainRole List">
        <Datagrid>
            <NumberField source="domain_id" />
            <TextField source="invitation_id" />
            <NumberField source="role_id" />
            <DateField source="updated_at" />
            <DateField source="created_at" />
        </Datagrid>
    </List>
)

export const InvitationDomainRoleShow = props => (
    <Show {...props} title="InvitationDomainRole Show">
        <SimpleShowLayout>
            <NumberField source="domain_id" />
            <TextField source="invitation_id" />
            <NumberField source="role_id" />
            <DateField source="updated_at" />
            <DateField source="created_at" />
        </SimpleShowLayout>
    </Show>
)

export const InvitationDomainRoleCreate = props => (
    <Create {...props} title="Create InvitationDomainRole">
        <SimpleForm validate={validationCreateInvitationDomainRole}>
            <NumberInput source="domain_id" />
            <TextInput source="invitation_id" />
            <NumberInput source="role_id" />
        </SimpleForm>
    </Create>
)

