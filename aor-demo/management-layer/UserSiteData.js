import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    DateField,
    DateInput,
    NumberField,
    NumberInput,
    TextField,
    TextInput,
    BooleanField,
    BooleanInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateUserSiteData = values => {
    const errors = {};
    if (!values.user_id) {
        errors.user_id = ["user_id is required"];
    }
    if (!values.site_id) {
        errors.site_id = ["site_id is required"];
    }
    return errors;
}

const validationEditUserSiteData = values => {
    const errors = {};
    return errors;
}

export const UserSiteDataList = props => (
    <List {...props} title="UserSiteData List">
        <Datagrid>
            <DateField source="updated_at" />
            <NumberField source="site_id" />
            <DateField source="consented_at" />
            <TextField source="user_id" />
            <BooleanField source="blocked" />
            <DateField source="created_at" />
            <EditButton />
        </Datagrid>
    </List>
)

export const UserSiteDataShow = props => (
    <Show {...props} title="UserSiteData Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <NumberField source="site_id" />
            <DateField source="consented_at" />
            <TextField source="user_id" />
            <BooleanField source="blocked" />
            <DateField source="created_at" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const UserSiteDataCreate = props => (
    <Create {...props} title="Create UserSiteData">
        <SimpleForm validate={validationCreateUserSiteData}>
            <TextInput source="user_id" />
            <BooleanInput source="blocked" />
            <TextInput source="consented_at" />
            <NumberInput source="site_id" />
        </SimpleForm>
    </Create>
)

export const UserSiteDataEdit = props => (
    <Edit {...props} title="Edit UserSiteData">
        <SimpleForm validate={validationEditUserSiteData}>
            <BooleanInput source="blocked" />
            <TextInput source="consented_at" />
        </SimpleForm>
    </Edit>
)

