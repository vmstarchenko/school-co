/**
 * 
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { SchoolRequest } from './schoolRequest';


export interface PupilRequest { 
    /**
     * ФИО
     */
    fullName: string;
    /**
     * класс
     */
    educationLevel: number;
    school: SchoolRequest;
}
