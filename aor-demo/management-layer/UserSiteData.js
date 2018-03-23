import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    BooleanField,
    DateField,
    TextField,
    NumberField,
    BooleanInput,
    TextInput,
    NumberInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
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
            <BooleanField source="blocked" />
            <DateField source="updated_at" />
            <ReferenceField label="User" source="user_id" reference="users" allowEmpty>
                <TextField source="id" />
            </ReferenceField>
            <DateField source="consented_at" />
            <DateField source="created_at" />
            <ReferenceField label="Site" source="site_id" reference="sites" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const UserSiteDataCreate = props => (
    <Create {...props} title="UserSiteData Create">
        <SimpleForm validate={validationCreateUserSiteData}>
            <BooleanInput source="blocked" />
            <ReferenceInput label="User" source="user_id" reference="users" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
            <ReferenceInput label="Site" source="site_id" reference="sites" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
            <TextInput source="consented_at" />
        </SimpleForm>
    </Create>
)

export const UserSiteDataShow = props => (
    <Show {...props} title="UserSiteData Show">
        <SimpleShowLayout>
            <BooleanField source="blocked" />
            <DateField source="updated_at" />
            <ReferenceField label="User" source="user_id" reference="users" allowEmpty>
                <TextField source="id" />
            </ReferenceField>
            <DateField source="consented_at" />
            <DateField source="created_at" />
            <ReferenceField label="Site" source="site_id" reference="sites" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
        </SimpleShowLayout>
    </Show>
)

export const UserSiteDataEdit = props => (
    <Edit {...props} title="UserSiteData Edit">
        <SimpleForm validate={validationCreateUserSiteData}>
            <BooleanInput source="blocked" />
            <TextInput source="consented_at" />
        </SimpleForm>
    </Edit>
)

