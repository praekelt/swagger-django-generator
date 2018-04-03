/**
 * Generated UserSiteData.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Datagrid,
    ReferenceField,
    TextField,
    NumberField,
    DateField,
    LongTextField,
    BooleanField,
    SimpleForm,
    Create,
    ReferenceInput,
    SelectInput,
    BooleanInput,
    LongTextInput,
    Show,
    SimpleShowLayout,
    Edit,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import DateTimeInput from 'aor-datetime-input';
import {
    UserSiteDataFilter
} from './Filters';

const validationCreateUserSiteData = values => {
    const errors = {};
    if (!values.user_id) {
        errors.user_id = ["user_id is required"];
    }
    if (!values.site_id) {
        errors.site_id = ["site_id is required"];
    }
    if (!values.data) {
        errors.data = ["data is required"];
    }
    return errors;
}

const validationEditUserSiteData = values => {
    const errors = {};
    return errors;
}

export const UserSiteDataList = props => (
    <List {...props} title="UserSiteData List" filters={<UserSiteDataFilter />}>
        <Datagrid>
            <ReferenceField label="User" source="user_id" reference="users" linkType="show" allowEmpty>
                <TextField source="username" />
            </ReferenceField>
            <ReferenceField label="Site" source="site_id" reference="sites" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <DateField source="consented_at" />
            <LongTextField source="data" />
            <BooleanField source="blocked" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const UserSiteDataCreate = props => (
    <Create {...props} title="UserSiteData Create">
        <SimpleForm validate={validationCreateUserSiteData}>
            <ReferenceInput label="User" source="user_id" reference="users" allowEmpty>
                <SelectInput source="id" optionText="username" />
            </ReferenceInput>
            <ReferenceInput label="Site" source="site_id" reference="sites" allowEmpty>
                <SelectInput source="id" optionText="name" />
            </ReferenceInput>
            <DateTimeInput source="consented_at" />
            <BooleanInput source="blocked" />
            <LongTextInput source="data" format={value => value instanceof Object ? JSON.stringify(value) : value} parse={v => { try { return JSON.parse(v); } catch (e) { return v; } }} />
        </SimpleForm>
    </Create>
)

export const UserSiteDataShow = props => (
    <Show {...props} title="UserSiteData Show">
        <SimpleShowLayout>
            <ReferenceField label="User" source="user_id" reference="users" linkType="show" allowEmpty>
                <TextField source="username" />
            </ReferenceField>
            <ReferenceField label="Site" source="site_id" reference="sites" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <DateField source="consented_at" />
            <LongTextField source="data" />
            <BooleanField source="blocked" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
        </SimpleShowLayout>
    </Show>
)

export const UserSiteDataEdit = props => (
    <Edit {...props} title="UserSiteData Edit">
        <SimpleForm validate={validationEditUserSiteData}>
            <DateTimeInput source="consented_at" />
            <BooleanInput source="blocked" />
            <LongTextInput source="data" format={value => value instanceof Object ? JSON.stringify(value) : value} parse={v => { try { return JSON.parse(v); } catch (e) { return v; } }} />
        </SimpleForm>
    </Edit>
)

/** End of Generated Code **/